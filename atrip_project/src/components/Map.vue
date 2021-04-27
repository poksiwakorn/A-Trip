<template>
  <div>
    <h3>{{onana}}</h3>
    <!-- <h2>FUCK</h2> -->
    <!-- <h1>{{markers}}</h1> -->
  
    <!-- <p>{{ coordinates.lat }} Latitude , {{ coordinates.lng }} Longitude</p> -->
    <GmapMap
      :center="centerPosition"
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
      v-for="(m, index) in loca"
      :key="index"
      :position="m"
      :clickable="true"
      :draggable="false"
      @click="centerPosition=m"
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
    centerPosition: this.loca[0],
      markers :[
          { position : this.loca },
          { position : { lat: 13.404735200000003, lng: 101.0049182 } },
          { position : { lat: 13.504735200000003, lng: 101.0049182 } }
        ],
    };
  },
  methods: {
      drawMarker(){
          this.markers = [
              
          ]
      },
  },
  
  // created: function(){
  //   this.$getLocation({})
  //     .then((coordinates) => {
  //       this.coordinates = coordinates;
  //     })
  //     .catch((error) => alert(error));
  // },

  props:[
      "loca"  , "onana"   
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
