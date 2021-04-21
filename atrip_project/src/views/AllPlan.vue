<template>
  <v-content>
    <TripBar/>
    <div class="AllPlan">
        <v-row class="ml-5 mt-1">
          <v-col cols = "12">
            <v-btn color = "primary" class="choose-btn">
              Choose district you want
            </v-btn>
          </v-col>
          <v-col cols="7">
            <v-card >
              <v-card-title class="white--text orange darken-4 text-h4">
                Interesting Trips
                <v-spacer></v-spacer>
                <v-text-field
                  placeholder="Search..."
                  solo
                  clearable
                  color = "orange"
                  class = "search-field"
                ></v-text-field>
                <!-- <v-btn icon color="white">
                  <v-icon>mdi-magnify</v-icon>
                </v-btn> -->
              </v-card-title>
              
              <v-divider></v-divider>
              <v-virtual-scroll
                :items = "items"
                :item-height = "1000"
                height = "480"
                class="my-5"
              >
                <!-- <template v-slot:default = "{item}">
                  <v-list-item>
                    <img src = "../assets/sea1.jpg" class="img_content">
                    <v-list-item-content>
                      {{item}}
                    </v-list-item-content>
                  </v-list-item>
                </template> -->
                <v-col
                  v-for = "(item, i) in items"
                  :key = "i"
                  cols="6"
                >
                  <v-card>
                    <v-img src = "../assets/sea1.jpg" height="200px"></v-img>
                    <v-card-title>
                      {{item.title}}
                      <v-spacer></v-spacer>
                      <v-chip class="ma-2" color="#FF9100" outlined>Suratthani</v-chip>
                      <v-chip class="ma-2" color="#FF9100" outlined>Bankok</v-chip>
                    </v-card-title>                    
                    <v-card-subtitle>CrazyboyOO1</v-card-subtitle>
                    <v-card-subtitle class="black--text">4 Places</v-card-subtitle>
                    <v-btn color="#FF9100" outlined class="ma-2">view info <v-icon class="ml-2">mdi-clipboard-text-search-outline</v-icon></v-btn>
                    <v-btn icon color="#FF9100"><v-icon>mdi-thumb-up</v-icon></v-btn>
                  </v-card>
                </v-col>
              </v-virtual-scroll>
            </v-card>
          </v-col>
          <!-- RIGHT -->
          <v-col cols="4" class="ml-13">
            <v-card>
              <v-img src = "../assets/gallery1.jpg" height="200px"></v-img>
              <v-card-title>
                Musuem Of Contemporary Art (MOCA)
                <v-spacer></v-spacer>
                <v-chip outlined >Bankok</v-chip>
              </v-card-title>
              <v-divider class="mx-4"></v-divider>
              <v-card-text class="text--primary ma-2">Place Description</v-card-text>
              <v-card-action>
                <v-btn color="#FF9100" text class="ma-2">EXPLORE</v-btn>
              </v-card-action>
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
  name: "AllPlan",
  components: {
    TripBar
  },

  data: () => ({
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
      }
    ]
  }),
};
</script>

<style scoped>
  .choose-btn{
    margin-top: 73px;
  }

  .img_content{
    width: 250px;
    height: 125px;
  }

  .title{
    font-size: 100px;
  }

  .search-field{
    background-color: rgb(255, 255, 255,100);
    width: 200px;
    height: 48px;
  }

  .inner-img{
    height: 200px;
  }

</style>