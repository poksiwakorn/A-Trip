<template>
  <div class="Register">
    <v-row>
      <v-col cols = "6">
        <img class="img1" />
      </v-col>
      <v-col cols = "6">
        <v-form class="register-form" v-model="valid">
          <span class="text1">Register</span>
          <v-text-field
            v-model="username"
            label="Username"
            placeholder="Username"
            :rules="usernameRule"
            regular
            class="mb-3"
            required
          ></v-text-field>
          <v-text-field
            label="Password"
            placeholder="Password1234"
            :rules="passwordRule"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showPassword ? 'text' : 'password'"
            regular
            class="mt-7 mb-3"
            @click:append="showPassword = !showPassword"
          ></v-text-field>
          <v-row>
            <v-col cols="6">
              <v-text-field
                label="Firstname"
                placeholder="Firstname"
                :rules="firstnameRule"
                regular
                class="mt-7 mb-3"
              ></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field
                label="Lastname"
                placeholder="Lastname"
                :rules="lastnameRule"
                regular
                class="mt-7 mb-3"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-menu v-model="dateMenu" absolute>
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                label="Birthday"
                placeholder="dd/mm/yy"
                regular
                class="mt-7 mb-3"
                prepend-icon="mdi-calendar-range"
                slot="activator"
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker></v-date-picker>
          </v-menu>
          <v-text-field
            label="Email"
            placeholder="myEmail@hotmail.com"
            regular
            class="mt-7 mb-3"
          ></v-text-field>
          <v-btn text color="#F57F17" class="btn1" link to="/Home"
            >Submit</v-btn
          >
        </v-form>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "Register",
  data: () => ({
    valid: false,
    showPassword: false,
    usernameRule: [
      (v) => !!v || "Username is required",
      (v) => v.length <= 10 || "Username must be less than 10 characters",
    ],
    passwordRule: [
      (v) => !!v || "Password is required",
      (v) => v.length <= 10 || "Password must be less than 10 characters",
    ],
    firstnameRule: [
      (v) => !!v || "Firstname is required",
      (v) => v.length <= 10 || "Firstname must be less than 10 characters",
    ],
    lastnameRule: [
      (v) => !!v || "Lastname is required",
      (v) => v.length <= 10 || "Lastname must be less than 10 characters",
    ],
  }),
};
</script>


<style scoped>
.text1 {
  font-weight: 500;
  font-size: 40px;
  line-height: 129px;
  text-align: center;
  color: #000000;
  text-shadow: 0px 6px 4px rgba(0, 0, 0, 0.1);
  transition: 770ms cubic-bezier(0.55, 0.055, 0.675, 0.19);
}

.img1 {
  /* position: absolute; */
  width: 100%;
  height: 950px;

  background: url(../assets/temple1.jpg);
  background-repeat: no-repeat;
  background-size: 100%;
}

.btn1 {
  left: 300px;
  top: 30px;
  font-size: 20px;
}

.register-form {
  width: 400px;
  margin-left: 25%;
}
</style>
