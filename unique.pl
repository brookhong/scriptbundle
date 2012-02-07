use strict;
use warnings;
use Digest::MD5;
use File::Find;
use Config::IniFiles;
use File::Basename;
use Cwd 'abs_path';

@ARGV = ('.') unless @ARGV;
my $g_refresh_inifile = 0;
my $g_purge = 0;
my $g_iniFileName = abs_path(basename(__FILE__)).".ini";
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

	my $section = substr($digest,0,1);
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
		$log->WriteConfig($g_iniFileName.".tmp");
	}
	close FILE;
}
sub usage() {
	print "perl ".basename(__FILE__)." -u\n\t--Show usage.\n";
	print "perl ".basename(__FILE__)." -f\n\t--Check and refresh ini files.\n";
	print "perl ".basename(__FILE__)." [-p] <path_to_purge>\n\t--Unique it, remove duplicate files with -p.\n";
	exit 1;
}

while ( my $arg = shift @ARGV ) {
	if($arg =~ /-(.)/) {
		if ($1 eq 'f') {
			checkDeadFile($g_iniFileName);
			exit 1;
		} elsif ($1 eq 'p') {
			$g_purge = 1;
		} elsif ($1 eq 'u') {
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
find(\&digestFile, @ARGV) if @ARGV;
rename "$g_iniFileName.tmp", $g_iniFileName;
