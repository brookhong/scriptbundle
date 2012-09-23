jQuery(document).ready(function() {
  var classes = ['maxheight','maxwidth',''];
  jQuery('img').click(function() {
    var m = jQuery(this);
    var s = m.width()+", "+m.height();
    var j = parseInt(m.attr('cid'))+1;
    for(var i=0; i<3; i++) {
      j = (j+i)%3;
      m.attr('class', classes[j]);
      if( s != m.width()+", "+m.height() ) {
        break;
      }
    }
    m.attr('cid', j);
    jQuery('#view_info').html(classes[j]);
  });
  jQuery('img').bind("contextmenu",function(e){
    window.location.reload(true);
    return false;
  });
  jQuery(document).keydown(function(e){
    if(e.which == 70 && jQuery(e.target).attr('id') != 'tag') {
      jQuery('#toolbars').fadeToggle();
    }
  });
});
