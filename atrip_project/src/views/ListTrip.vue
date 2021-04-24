<template>
  <v-content>
    <TripBar />
    <div class="ListTrip">
      <div class="chipBar">
        <v-chip-group
            active-class="chipActive white--text"
            v-model = "typeGroup"
        >
        <v-chip v-for="type in types" :key="type">{{ type }}</v-chip>
        </v-chip-group>
      </div>
      <v-row>
        <v-col cols="4" class="mapCard">
          <v-card>
            <!-- <v-img src = "..assets/map1.png" height="200px"></v-img> -->
          </v-card>
        </v-col>
        <v-col cols="3" class="listCard">
          <v-row v-for="(place, i) in places" :key="i">
            <v-card v-if="place.info.includes(types[typeGroup]) || types[typeGroup] == 'All'" class="ma-3">
              <v-img :src = "place.src[0]" class="placePic"></v-img>
              <v-card-title>
                {{ place.title }}
                <v-spacer></v-spacer>
                <v-chip class="ma-2" color="#FF9100" outlined>{{place.province}}</v-chip>
              </v-card-title>
              <v-card-subtitle>{{place.info}}</v-card-subtitle>
              <v-btn color="#FF9100" outlined class="ma-2" link to = "/PlaceInfo"
                >view info
                <v-icon class="ml-2">mdi-clipboard-text-search-outline</v-icon>
              </v-btn>
              <v-btn color="#FF9100" outlined class="ma-2" @click="addPlace(place)"
                >ADD TO TRIP
                <v-icon class="ml-2">mdi-plus-outline</v-icon>
              </v-btn>
              <!-- <v-btn icon color="#FF9100"><v-icon>mdi-thumb-up</v-icon></v-btn> -->
            </v-card>
          </v-row>
        </v-col>
        <v-col cols="5" class="tripCard">
          <v-card class="ma-3">
            <v-card-title class="yourTripTitle white--text">Your Trip</v-card-title>
            <v-divider></v-divider>
            <v-form class="mt-1">
              <v-row>
                <v-col cols = "4">
                  <v-card-title>Trip's Name</v-card-title>
                </v-col>
                <v-col cols = "6">
                  <v-text-field regular placeholder="myTrip" color="orange" required clearable></v-text-field>
                </v-col>
              </v-row>
              <v-card-subtitle>Please choose at least 2 places</v-card-subtitle>
              <v-card class="scrollCard">
                <v-virtual-scroll
                  page-mode
                  :items = "placesInTrip"
                  :item-height = "150"
                  height = "566"
                >
                  <template v-slot = "place">
                    <v-row>
                      <v-col cols = "2" class="ml-2">
                        <v-card class="numberCard mb-5">
                          {{place.index+1}}
                        </v-card>
                      </v-col>
                      <v-col cols = "4">
                        <v-card class="mb-5">
                          <v-img :src = "getItem(places,place.item).src[0]" class="placeImage"></v-img>
                        </v-card>
                      </v-col>
                      <v-col cols = "5">
                        <v-card class="mt-3">
                          <v-row>
                            <v-card-title class="ml-2" style="font-weight: 400">{{place.item}}</v-card-title>
                            <v-spacer></v-spacer>
                            <v-btn icon class="mt-3 mr-4" @click="canclePlace(place.index)"><v-icon color = "error">mdi-close</v-icon></v-btn>
                          </v-row>
                          <v-chip class="ma-2" color="#FF9100" outlined>{{getItem(places,place.item).province}}</v-chip>
                        </v-card>
                      </v-col>
                    </v-row>
                  </template>
                </v-virtual-scroll>
              </v-card>
              <v-row>
                <v-btn text class="makeTripButton" link to="/account">Make A Trip</v-btn>
                <v-spacer></v-spacer>
                <v-btn text class="updateButton">Update Route</v-btn>
              </v-row>
            </v-form>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </v-content>
</template>

<script>
// @ is an alias to /src
import TripBar from "../components/TripBar";

export default {
  name: "ListTrip",
  components: {
    TripBar,
  },

  data: () => ({
    types: ["All","Photograph", "Restaurant", "Residence"],
    typeGroup: 0,
    placesInTrip: [],
    places: [
      {
        src: [require("../assets/aquarium1.jpg")],
        title: "AQUARIUM",
        info: "Photograph",
        province: "Bangkok"
      },
      {
        src: [require("../assets/island1.jpg")],
        title: "ISLAND",
        info: "Photograph,Residence,Restaurant",
        province: "Phuket"
      },
      {
        src: [require("../assets/market1.jpg")],
        title: "MARKET",
        info: "Photograph,Restaurant",
        province: "China"
      },
      {
        src: [require("../assets/passage1.jpg")],
        title: "PASSAGE",
        info: "Photograph,Residence",
        province: "Newzeland"
      },
      {
        src: [require("../assets/road1.jpg")],
        title: "ROAD",
        info: "Photograph",
        province: "Bangkok"
      },
      {
        src: [require("../assets/sea1.jpg")],
        title: "SEA",
        info: "Photograph,Residence,Restaurant",
        province: "Suratthani"
      },
      {
        src: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Opensource.svg/1200px-Opensource.svg.png",
        title: "TEMPLE",
        info: "Photograph",
        province: "Nakornsitammarat"
      },
    ],
  }),
  methods: {
    addPlace: function(item){
      this.placesInTrip.push(item.title);
    },
    canclePlace: function(index){
      this.placesInTrip.splice(index,1);
    },
    getItem: function(items,item){
      for(var i=0;i<items.length;i++){
        if(items[i].title == item){
          return items[i];
        }
      }
    }
  }
};
</script>

<style scoped>
    .chipBar {
      margin: 10px;
      position: fixed;
      margin-top: 83px;
    }

    .chipActive {
      background-color: #ff9100;
    }

    .mapCard {
      position: fixed;
      width: 100%;
      height: 630px;
      margin-top: 123px;
      margin-left: 10px;
    }

    .mapPic {
      background-image: url(../assets/map1.png);
    }

    .listCard {
      position: absolute;
      margin-top: 123px;
      left: 33vw;
    }

    .placePic{
      width: 800px;
      height: 280px;
    }

    .tripCard {
      position: fixed;
      /* margin-top: 70px;
      margin-left: 905px; */
      top: 7%;
      left: calc(59% - 10px);
    }

    .yourTripTitle{
      background-color: #faae4b;
      font-size: 30px;
    }

    .numberCard{
      background-color: #faae4b;
      color: black;
      font-size: 45px;
      font-weight:80;
      text-align: center;
      padding-top: 25%;
      height: 87%;
    }

    .scrollCard{
      margin-left: 20px;
      padding-left: 15px;
      padding-top: 15px;
      padding-bottom: 15px;
      width: 95%;
      height: 60vh;
    }

    .makeTripButton{
      margin-left: 45px;
      margin-top: 30px;
      margin-bottom: 15px;
      color: #ff9100;
    }

    .updateButton{
      margin-right: 40px;
      margin-top: 30px;
      margin-bottom: 15px;
      color: #ff9100;
    }

    .placeImage{
      width: 100%px;
      height: 100px;
    }
</style>