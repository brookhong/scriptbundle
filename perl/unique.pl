use strict;
use warnings;
use Digest::MD5;
use File::Find;
use Config::IniFiles;
use File::Basename;
use Cwd 'abs_path';

# @ARGV = ('.') unless @ARGV;
my $g_target_path = "";
my $g_purge = 0;
my $g_rename = 0;
my $g_iniFileName = $ENV{"HOME"}."/".basename(__FILE__).".ini";
my $log = Config::IniFiles->new() or die "Failure: @Config::IniFiles::errors\n";

sub checkDeadFile {
	my ($iniFile) = @_;
	open(OUTFILE, ">$iniFile.new");
	open FILE, "<".$iniFile or die $!;
	while (<FILE>) {
		if($_ =~ /.{32}=(.*)\n/si) {
			if(-e $1) {
				print OUTFILE $_;
			}
			else {
				print "[info] File $1 does not exist!\n";
			}
		}
		else {
			print OUTFILE $_;
		}
	}
	close FILE;
	unlink $iniFile;
	rename "$iniFile.new", $iniFile;
	print "[info] $iniFile ok!\n";
}
sub digestFile {
	return unless -f;
	my $digestObj = new Digest::MD5;

	open(FILE, "<".$_);

	$digestObj->addfile(*FILE);
	my $digest = $digestObj->hexdigest;
	close FILE;

	my $section = substr($digest,0,1);
	if($g_rename) {
		my $newName = $_;
		$newName =~ s/.*\.(.*)$/$digest\.$1/;
		my $sourceName = "";
		if($g_target_path ne "") {
			$sourceName = $File::Find::name;
			my $subDir = substr($newName,0,2);
			$subDir = "$g_target_path/$subDir";
			if (! -e $subDir) {
				mkdir $subDir;
			}
			$newName = "$subDir/$newName";
		} elsif($_ ne $newName) {
			$sourceName = $_;
		}
		if($sourceName ne "") {
			print "rename $sourceName, $newName\n";
			rename $sourceName, $newName;
		}
	}
	else {
		my $val = $log->val($section, $digest);
		if (defined($val)) {
			print $digest." <= ".$File::Find::name." same as $val\n";
			if($g_purge) {
				print "[info] delete $File::Find::name.\n";
				unlink $File::Find::name;
			}
		}
		else {
			$log->newval($section, $digest, $File::Find::name);
			$log->WriteConfig($g_iniFileName);
		}
	}
}
sub usage() {
	print "perl ".basename(__FILE__)." -h\n\t--Show usage.\n";
	print "perl ".basename(__FILE__)." -f\n\t--Check and refresh ini files.\n";
	print "perl ".basename(__FILE__)." [-p] <path_to_purge>\n\t--Unique it, remove duplicate files with -p.\n";
	print "perl ".basename(__FILE__)." [-r] <path_to_purge>\n\t--Unique it, rename all the files with -r.\n";
	print "perl ".basename(__FILE__)." [-t <target_path>] [-r] <path_to_purge>\n\t--Unique it, rename all the files with -r, and move the file to <target_path>.\n";
	print "\tperl ".basename(__FILE__)." -r -t unified/ downloads/\n";
	exit 1;
}

while ( my $arg = shift @ARGV ) {
	if($arg =~ /-(.)/) {
		if ($1 eq 'f') {
			checkDeadFile($g_iniFileName);
			exit 1;
		} elsif ($1 eq 'p') {
			$g_purge = 1;
		} elsif ($1 eq 't') {
			$g_target_path = shift @ARGV;
			$g_target_path = abs_path($g_target_path);
		} elsif ($1 eq 'r') {
			$g_rename = 1;
		} elsif ($1 eq 'h') {
			usage();
		} else {
			usage();
		}
	}
	else {
		unshift @ARGV,$arg;
		last;
	}
}
if (@ARGV){
	my $path = abs_path(@ARGV);
	find(\&digestFile, $path);
}
else {
	usage();
}
