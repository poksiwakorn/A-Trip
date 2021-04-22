<template>
  <div class="Register">
    <img class="img1" />
    <v-form class="register-form" v-model="valid">
      <span class="text1">Register</span>
      <v-text-field
        v-model = "form.username"
        label="Username"
        placeholder="Username"
        :rules = "usernameRule"
        regular
        class = "mb-3"
        required
      ></v-text-field>
      <v-text-field
        v-model = "form.password"
        label="Password"
        placeholder="Password1234"
        :rules = "passwordRule"
        :append-icon = "showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        :type = "showPassword ? 'text' : 'password'"
        regular
        class="mt-7 mb-3"
        @click:append = "showPassword = !showPassword"
      ></v-text-field>
      <v-row>
        <v-col cols="6">
          <v-text-field
            v-model = "form.firstname"
            label="Firstname"
            placeholder="Firstname"
            :rules = "firstnameRule"
            regular
            class="mt-7 mb-3"
          ></v-text-field>
        </v-col>
        <v-col cols="6">
          <v-text-field
            v-model = "form.lastname"
            label="Lastname"
            placeholder="Lastname"
            :rules = "lastnameRule"
            regular
            class="mt-7 mb-3"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-menu v-model="dateMenu" absolute>
        <template v-slot:activator = "{on,attrs}">
          <v-text-field
            label="Birthday"
            placeholder="dd/mm/yy"
            regular
            class="mt-7 mb-3"
            prepend-icon="mdi-calendar-range"
            slot = "activator"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker></v-date-picker>
      </v-menu>
      <v-text-field
        v-model = "form.email"
        label="Email"
        placeholder="myEmail@hotmail.com"
        regular
        class="mt-7 mb-3"
      ></v-text-field>
      <v-btn @click = "register" text color = "#F57F17" class="btn1">Submit</v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  name: "Register",
  methods: {
    async register(){
      try {
        await this.$store.dispatch("Register",this.form);
        if (this.$store.getters.StateMsg == "You have successfully registered!")
          this.$router.push("/SignIn");
        this.showMsg = true
      } catch (error) {
        this.showMsg = true
      }
    }
  },
  data: () => ({
    form: {
        username: "",
        password : "",
        firstname : "",
        lastname : "",
        email : ""
     },
    valid: false,
    showPassword: false,
    usernameRule: [
        v => !!v || 'Username is required',
        v => v.length <= 10 || 'Username must be less than 10 characters',
    ],
    passwordRule: [
        v => !!v || 'Password is required',
        v => v.length <= 10 || 'Password must be less than 10 characters',
    ],
    firstnameRule: [
        v => !!v || 'Firstname is required',
        v => v.length <= 10 || 'Firstname must be less than 10 characters',
    ],
    lastnameRule: [
        v => !!v || 'Lastname is required',
        v => v.length <= 10 || 'Lastname must be less than 10 characters',
    ]
  }
  ),
};
</script>


<style scoped>
  .text1{
    font-weight: 500;
    font-size: 40px;
    line-height: 129px;
    text-align: center;
    color: #000000;
    text-shadow: 0px 6px 4px rgba(0, 0, 0, 0.10);
    transition: 770ms cubic-bezier(0.55, 0.055, 0.675, 0.19)
  }

  .img1 {
    position: absolute;
    width: 700px;
    height: 754px;
    left: -1px;
    top: 0px;

    background: url(../assets/temple1.jpg);
    background-repeat: no-repeat;
    background-size: 100%;
  }

  .btn1{
    left: 300px;
    top: 30px;
    font-size: 20px;
  }

  .register-form {
    width: 400px;
    position: absolute;
    left: 920px;
    top: 30px;
  }
</style>
