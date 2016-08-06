// FUNCTIONS TO BE RUN AFTER PAGE HAS LOADED
$(document).ready(function() {   

/* LHS nav scrolls only to top of footer. Doesn't overlap */
var doc = $(document); 
doc.scroll(function () {
     
    var footer = $('#whole-ft');
    var p = $('#nav-fixed');
    var s = $('#left-nav-position');

    var top = doc.scrollTop() + s.offset().top  * 1.95 + p.height();
    var footerTop = footer.offset().top;

    var offset = footerTop - top;

    if (offset < 0) {
        p.css({'margin-top': '' + offset + 'px'});
    } else {
        p.css({'margin-top': 0});
    }
});
/* End of LHS nav scroll */

AmCharts.makeChart( "mapdiv_cusine", {
  /**
   * this tells amCharts it's a map
   */
  "type": "map",


  /**
   * create data provider object
   * map property is usually the same as the name of the map file.
   * getAreasFromMap indicates that amMap should read all the areas available
   * in the map data and treat them as they are included in your data provider.
   * in case you don't set it to true, all the areas except listed in data
   * provider will be treated as unlisted.
   */
    "dataProvider": {
    "map": "continentsLow",

    "areas": [
    { "id": "JP",
    "url": "recipes-jap.html"},
      { "id": "IN",
    "url": "recipes-indian.html"},
      { "id": "CN",
    "url": "recipes-chinese.html"},
    { "id": "HK",
    "url": "recipes-chinese.html"},
    { "id": "south_america",
    "url": "recipes-southa.html"},
    { "id": "north_america",
    "url": "recipes-northa.html"},
    { "id": "europe",
    "url": "recipes-europe.html"},
    { "id": "KP",
    "url": "recipes-korean.html"},
    { "id": "KR",
    "url": "recipes-korean.html"},
    { "id": "LB",
    "url": "recipes-lebanese.html"},
   
  ],
    // "getAreasFromMap": true,

  },

  /** 
   * create areas settings
   * autoZoom set to true means that the map will zoom-in when clicked on the area
   * selectedColor indicates color of the clicked area.
   */
  "areasSettings": {
    "unlistedAreasColor": "#BBBBBB",
    "rollOverOutlineColor": "#008080",
    "color": "rgba(129,216,208 , 1)",
    "autoZoom": true,
    "selectedColor": "#81D8D0",
    "bringForwardOnHover": false,
     
  },

  /**
   * let's say we want a small map to be displayed, so let's create it
  //  */
  // "smallMap": {}
} );

});