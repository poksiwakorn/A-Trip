<template>
  <div class="SignIn">
      <img class="bg-img">
      <v-form class="sign-in-form">
        <v-row>
          <v-col cols="12">
            <h1 style="font-size: 30px;" class="grey--text">ลงชื่อเข้าใช้งาน</h1>
          </v-col>     
          <v-col cols="12">
            <v-text-field
              v-model = "form.username"
              label="ชื่อผู้ใช้"
              placeholder="Username"
              :rules = "usernameRule"
              regular
              class = "mb-3"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              v-model = "form.password"
              label="รหัสผ่าน"
              placeholder="Password1234"
              :rules = "passwordRule"
              :append-icon = "showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :type = "showPassword ? 'text' : 'password'"
              regular
              class="mt-7 mb-3"
              @click:append = "showPassword = !showPassword"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-btn @click = "Login" align-center color="info" style="font-size: 20px;">ถัดไป</v-btn>
          </v-col>
          <v-col cols="12">
            <!-- <router-link to="/about">Forget your password?</router-link> -->
          </v-col>
          <v-col cols="12">
            <router-link to="/Register">ยังไม่มีรหัสอีกเหรอ? กดตรงนี้สิ</router-link>
          </v-col>
        </v-row>
      </v-form>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "SignIn",
  components: {},
  data() {
    return {
      form:{
        username: "",
        password : ""
      },
      showPassword: false,
      usernameRule: [
          v => !!v || 'Username is required',
          v => v.length <= 10 || 'Username must be less than 10 characters',
      ],
      passwordRule: [
          v => !!v || 'Password is required',
          v => v.length <= 10 || 'Password must be less than 10 characters',
      ]
    }
  },
  methods:{
    async Login(){
      try {
        await this.$store.dispatch("LogIn",this.form);
        if (this.$store.getters.isAuthenticated){
          this.$router.push("/Home")
        }
      }
      catch(error){
        console.log(error)
      }
    },
  },
};
</script>

<style scoped>
  .bg-img{
    position: absolute;
    width: 100vw;
    height: 100vh;
    left: 0px;
    top: 0px;
    
    background: url(../assets/login_bg.png);
    background-repeat: no-repeat;
    background-size: 100%;
  }

  .sign-in-form{
    position: absolute;
    width: 400px;
    left: 11vw;
    top: 45vh;
  }
</style>



