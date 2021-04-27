<template>
  <div>
    <h1>{{loca}}</h1>
    <h2>FUCK</h2>
    <h1>{{markers}}</h1>
  
    <!-- <p>{{ coordinates.lat }} Latitude , {{ coordinates.lng }} Longitude</p> -->
    <GmapMap
      :center="loca"
      :zoom="16"
      style=" width: 32vw; height:800px;"
      :options="{
            zoomControl: false,
            mapTypeControl: false,
            scaleControl: false,
           streetViewControl: true,
           rotateControl: false,
           fullscreenControl: false,
           disableDefaultUi: false
 }"
    
    >
    <GmapMarker
    v-for="(m, index) in markers"
    :key="index"
    :position="m.position"
    :clickable="true"
    :draggable="false"
    @click="center=m.position"
  />
  </GmapMap>
  </div>
</template>

<script>
const location = { lat: 13.404735200000003, lng: 101.0049182 };
export default {
  data() {
    return {
    //   coordinates: {
    //     lat: 0,
    //     lng: 0,
    //   },
      markers :[
          {
              position : { lat: loca.lat, lng: loca.lng }
          }
        ],
    };
  },
  methods: {
      drawMarker(){
          this.markers = [
              
          ]
      },
  },
//   created() {
//     this.$getLocation({})
//       .then((coordinates) => {
//         this.coordinates = coordinates;
//       })
//       .catch((error) => alert(error));
//   },

  props:[
      "loca"     
  ]
};
</script>

<style>
.mapCard {
      position: fixed;
      width: 32vw;
      height: 720px;
      margin-top:150px;
      margin-left: 10px;
    }
</style>
