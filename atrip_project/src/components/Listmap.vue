<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script>
export default {
  name: "Listmap",
  data() {
    return {
      map: null,
      markers: [],
      WP: [
        { location: "KMITL" },
        { location: "กรุงเทพ" },
        { location: "อ่างทอง" },
        { location: { lat: 13.784158268087618, lng: 100.69431020698494 } },
      ],
      coordinates: {
        getlat: 0,
        getlng: 0,
      },
      recenter: [
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
        this.recenter[0].lat = coordinates.lat;
        this.recenter[0].lng = coordinates.lng;
        this.initMap();
      })
      .catch((error) => alert(error));
  },
  methods: {
    initMap() {
      this.map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: this.recenter[0].lat, lng: this.recenter[0].lng },
        zoom: 12,
        mapTypeID: google.maps.MapTypeId.ROADMAP,
        zoomControl: false,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: true,
        rotateControl: false,
        fullscreenControl: false,
        disableDefaultUi: false,
      });

      // Click on the Map To Mark
    },
    addMarker: function(getlat, getlng) {
      // Add the marker at the clicked location, and add the next-available label
      // from the array of alphabetical characters.
      var markLatLng = new google.maps.LatLng(getlat, getlng);
      this.markers[markLatLng] = new google.maps.Marker({
        position: markLatLng,
        map: this.map,
        draggable: true,
        animation: google.maps.Animation.DROP,
      });
    },
    removeMarker(lat, long) {
      try {
        this.markers[new google.maps.LatLng(lat, long)].setMap(null);
      } catch (e) {}
    },
    moveToLocation(lat, lng) {
      const center = new google.maps.LatLng(lat, lng);
      this.map.panTo(center);
    },
  },
};
</script>
<style scoped>
#map {
  width: 32vw;
  height: 800px;
}
</style>
