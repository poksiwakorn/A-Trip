<template>
  <v-content>
    <TripBar/>
    <div class="ApprovePlace">
      <v-col cols="3" class="listCard">
          <v-row v-for="(place, i) in places" :key="i">
            <v-card v-if="place.isVerify == '0'" class="ma-3">
              <v-img src = "../assets/temple1.jpg" class="placePic"></v-img>
              <v-card-title>
                {{ place.nameTH }}
              </v-card-title>
              <v-card-title class="typeBar typeText">
                {{place.typeTH}} 
                <v-spacer></v-spacer>
                <v-chip class="ma-2" color="#FF9100" outlined>{{place.provinceTH}}</v-chip>
              </v-card-title>
              <v-card-subtitle>{{place.ownerID}}</v-card-subtitle>
              <v-btn color="#FF9100" outlined class="ma-2" link to = "/ApproveInfo"
                >view info
                <v-icon class="ml-2">mdi-clipboard-text-search-outline</v-icon>
              </v-btn>
            </v-card> 
          </v-row> 
        </v-col>
    </div>
  </v-content>
</template>

<script>
// @ is an alias to /src
import TripBar from "../components/TripBar";
import axios from "axios";

export default {
  name: "ApprovePlace",
  components: {
    TripBar
  },
  data: () => ({
    places: [
    ],
  }),
  methods: {
    async callPlaces(){
      await axios.post("location",{query:""}).then((res)=>this.places = res.data);
    }
  },

  created: function(){
    if(this.$store.getters.isAuthenticated){
      if(this.$store.getters.StateRole == 'Admin'){
        this.callPlaces();
      }else{
        this.$router.push('/Home');
      }
    }
    else{
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
    .listCard {
      position: absolute;
      margin-top: 7vh;
      left: 33vw;
    }

    .placePic{
      width: 800px;
      height: 280px;
    }

    .typeBar{
      margin-top: -35px;
    }

    .typeText{
      font-size: 20px;
      font-weight: 450;
    }
</style>