<template>
  <v-content>
    <TripBar />
    <div class="Account">
      <!-- <h1>This is Account page</h1> -->
      <v-row>
        <v-col cols="3">
          <v-card height="600" class="account_prf">
            <v-row justify="center">
              <v-avatar class="ma-10" color="primary" size="150"></v-avatar>
            </v-row>
            <v-row justify="center">
              <v-btn flat class="Btn1"> test btn1</v-btn>
            </v-row>
            <v-row justify="center">
              <v-btn flat class="Btn2"> test btn2</v-btn>
            </v-row>
          </v-card>
        </v-col>
        <v-col cols="8">
          <v-card color="orange lighten-4" class="saveTrip">
            <h1 class="saveTxt">Saved Trip</h1>
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
  name: "Account",
  components: {
    TripBar,
  },
};
</script>

<style scoped>
.account_prf {
  margin-left: 40px;
  margin-top: 60px;
}
.Btn2 {
  margin-left: 0px;
  margin-top: 20px;
  width: 300px;
}
.Btn1 {
  margin-left: 0px;
  margin-top: 250px;
  width: 300px;
}
.saveTrip{
  margin-left:70px;
  margin-top:50px;
  height:50px;
}
.saveTxt{
  margin-left:30px;
  margin-top:50px;
}
</style>