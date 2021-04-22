<template>
  <v-content>
    <TripBar />
    <div class="ListTrip">
      <div class="chipBar">
        <v-chip-group
            mandatory
            active-class="chipActive white--text"
        >
        <v-chip v-for="tag in tags" :key="tag">{{ tag }}</v-chip>
        </v-chip-group>
      </div>
      <v-row>
        <v-col cols="4">
          <div class="map"></div>
        </v-col>
        <v-col cols="3" class="listPlace">
          <v-row v-for="(item, i) in items" :key="i">
            <v-card class="ma-3">
              <v-img src="../assets/sea1.jpg" height="200px"></v-img>
              <v-card-title>
                {{ item.title }}
                <v-spacer></v-spacer>
                <v-chip class="ma-2" color="#FF9100" outlined>Suratthani</v-chip>
              </v-card-title>
              <v-card-subtitle>CrazyboyOO1</v-card-subtitle>
              <v-btn color="#FF9100" outlined class="ma-2" link to = "/PlaceInfo"
                >view info
                <v-icon class="ml-2">mdi-clipboard-text-search-outline</v-icon>
              </v-btn>
              <v-btn color="#FF9100" outlined class="ma-2" @click="addPlace(item)"
                >ADD TO TRIP
                <v-icon class="ml-2">mdi-plus-outline</v-icon>
              </v-btn>
              <v-btn icon color="#FF9100"><v-icon>mdi-thumb-up</v-icon></v-btn>
            </v-card>
          </v-row>
        </v-col>
        <v-col cols="5" class="yourTrip">
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
              <!-- <v-row v-for="(place, i) in placeInTrip" :key="i">
                <v-col>
                  {{place}}
                </v-col>
              </v-row> -->
              <v-card class="scrollCard">
                <v-virtual-scroll
                  page-mode
                  :items = "placeInTrip"
                  :item-height = "150"
                  height = "385"
                >
                  <template v-slot = "item">
                    <v-row>
                      <v-col cols = "2" class="ml-2">
                        <v-card class="numberCard mb-5">
                          <div>{{item.index+1}}</div>
                        </v-card>
                      </v-col>
                      <v-col cols = "4">
                        <v-card class="mb-5">
                          <v-img src = "../assets/sea1.jpg" class="placeImage"></v-img>
                        </v-card>
                      </v-col>
                      <v-col cols = "5">
                        <v-card class="mt-3">
                          <v-row>
                            <v-card-title class="ml-2" style="font-weight: 400">{{item.item}}</v-card-title>
                            <v-spacer></v-spacer>
                            <v-btn icon class="mt-3 mr-4" @click="canclePlace(item.index)"><v-icon color = "error">mdi-close</v-icon></v-btn>
                          </v-row>
                          <v-chip class="ma-2" color="#FF9100" outlined>Suratthani</v-chip>
                        </v-card>
                      </v-col>
                    </v-row>
                  </template>
                </v-virtual-scroll>
              </v-card>
              <v-row>
                <v-btn text class="makeTripButton">Make A Trip</v-btn>
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
    tags: ["All", "Restaurant", "Photograph", "Residence"],
    placeInTrip: [],
    items: [
      {
        src: "../assets/aquarium1.jpg",
        title: "AQUARIUM",
        info: "This is Aquarium",
      },
      {
        src: "../assets/island1.jpg",
        title: "ISLAND",
        info: "This is Island",
      },
      {
        src: "../assets/market1.jpg",
        title: "MARKET",
        info: "This is Market",
      },
      {
        src: "../assets/passage1.jpg",
        title: "PASSAGE",
        info: "This is Passage",
      },
      {
        src: "../assets/road1.jpg",
        title: "ROAD",
        info: "This is Road",
      },
      {
        src: "../assets/sea1.jpg",
        title: "SEA",
        info: "This is Sea",
      },
      {
        src: "../assets/temple1.jpg",
        title: "TEMPLE",
        info: "This is Temple",
      },
    ],
  }),
  methods: {
    addPlace: function(item){
      this.placeInTrip.push(item.title);
    },
    canclePlace: function(index){
      console.log(index);
      console.log(this.placeInTrip[index]);
      console.log(this.placeInTrip.splice(index,1));
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

    .map {
      position: fixed;
      width: 500px;
      height: 630px;
      margin-top: 123px;
      background-image: url(../assets/map1.png);
    }

    .listPlace {
      margin-top: 123px;
    }

    .yourTrip {
      position: fixed;
      margin-top: 70px;
      margin-left: 905px;
    }

    .yourTripTitle{
      background-color: #faae4b;
      font-size: 30px;
    }

    .numberCard{
      background-color: #faae4b;
      color: black;
      text-align: center;
      padding-top: 35%;
      font-size: 45px;
      font-weight:80;
      height: 87%;
    }

    .scrollCard{
      margin-left: 20px;
      padding-left: 15px;
      padding-top: 15px;
      padding-bottom: 15px;
      width: 550px;
      height: 400px;
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
      width: 200px;
      height: 100px;
    }
</style>