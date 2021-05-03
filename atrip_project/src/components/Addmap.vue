<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script>
export default {
  name: "Addmap",
  data() {
    return {
      map: null,
      marker: new google.maps.Marker(),
      markerlocation: null,
      coordinates: {
        getlat: 0,
        getlng: 0,
      },
      userlocation: [
        {
          lat: 0,
          lng: 0,
        },
      ],
    };
  },
  created: function() {
    this.$getLocation({})
      .then((coordinates) => {
        this.coordinates = coordinates;
        this.userlocation[0].lat = coordinates.lat;
        this.userlocation[0].lng = coordinates.lng;
      })
      .catch((error) => alert(error));
  },
  methods: {
    initMap() {
      this.map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 13.405053591362147, lng: 101.00503381648156 },
        zoom: 14,
        mapTypeID: google.maps.MapTypeId.ROADMAP,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: true,
        rotateControl: false,
        fullscreenControl: false,
        disableDefaultUi: false,
      });
      // this.marker = new google.maps.Marker({
      //   position: { lat: this.userlocation[0].lat, lng: this.userlocation[0].lat },
      //   map: this.map,
      //   draggable: true,
      //   animation: google.maps.Animation.DROP,
      // });
      console.log(this.userlocation);
      // Click on the Map To Mark
      google.maps.event.addListener(this.map, "click", (event) => {
        this.addMarker(event.latLng, this.map);
      });
    },
    addMarker: function(location, map) {
      // Add the marker at the clicked location, and add the next-available label
      // from the array of alphabetical characters.
      this.marker.setMap(null);
      
      this.marker = new google.maps.Marker({
        position: location,
        map: this.map,
        draggable: true,
        animation: google.maps.Animation.DROP,
      });
    },
    
  },
  mounted() {
    this.$getLocation({})
      .then((coordinates) => {
        this.coordinates = coordinates;
        this.userlocation[0].lat = coordinates.lat;
        this.userlocation[0].lng = coordinates.lng;
      })
      .catch((error) => alert(error));
    this.initMap();
  },

  // " Get Location User "
};
</script>
<style scoped>
#map {
  width: 37vw;
  height: 300px;
}
</style>
