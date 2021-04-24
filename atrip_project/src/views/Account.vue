<template>
  <v-content>
    <TripBar />
    <div class="Account">
      <v-row>
        <v-col cols="3">
          <v-card class="account_prf test">
            <v-row justify="center">
              <v-avatar class="ma-10" color="primary" size="150"></v-avatar>
            </v-row>
            <v-row justify="center">
              <v-btn flat class="Btn1">ทริปของคุณ</v-btn>
            </v-row>
            <v-row justify="center">
              <v-btn flat class="Btn2">แก้ไขข้อมูลส่วนตัว</v-btn>
            </v-row>
          </v-card>
        </v-col>
        <v-col cols="8">
          <v-card color="orange lighten-4" class="saveTrip">
            <h1 class="saveTxt">Saved Trip</h1>
          </v-card>
          <v-col cols="6">
            <v-slide-group
              v-model="model"
              class="pa-9"
              active-class="success"
              show-arrows
            >
              <v-slide-item v-for="n in 15" :key="n">
                <v-card
                  :color="active ? undefined : 'grey lighten-1'"
                  class="group ma-4"
                  @click="toggle"
                >
                </v-card>
              </v-slide-item>
            </v-slide-group>
          </v-col>
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
.Account {
  position: absolute;
  top: 63px;
}
.account_prf {
  margin-left: 40px;
  margin-top: 60px;
  height: 600px;
  width: 1300px;
}
.group {
  height: 450px;
  width: 0px;
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
.saveTrip {
  margin-left: 70px;
  margin-top: 50px;
  height: 50px;
}
.saveTxt {
  margin-left: 30px;
  margin-top: 50px;
}
.saveTxt2 {
  margin-left: 30px;
  margin-top: 50px;
}
/*@media screen and (max-width: 992px) {
  .account_prf {
    background-color: blue;
    color: white;
  }
}
@media screen and (max-width: 600px) {
  .account_prf {
    background-color: rgb(80, 229, 255);
    /* color: white; */
  /* } */
/* } */
</style>