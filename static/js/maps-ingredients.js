// FUNCTIONS TO BE RUN AFTER PAGE HAS LOADED
$(document).ready(function() {  

AmCharts.makeChart( "mapdiv_ingredients", {
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
    "url": "ingredients/japanese.html"},
      { "id": "IN",
    "url": "ingredients/indian.html"},
      { "id": "CN",
    "url": "ingredients/chinese.html"},
    { "id": "HK",
    "url": "ingredients/chinese.html"},
    { "id": "south_america",
    "url": "ingredients/south-american.html"},
    { "id": "KP",
    "url": "ingredients/korean.html"},
    { "id": "KR",
    "url": "ingredients/korean.html"},
   
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