import axios from "axios";

const state = {
  IsLogIn: false,
  Username: "",
  FirstName: "",
  LastName: "",
  Nickname: "",
  Email: "",
  Tel: "",
  Tag: "",
  Rating: "",
  Checkin: "",
  Favorite: "",
  Role: "",
  Msg: ""
};

const getters = {
  StateUsername: (state) => state.Username,
  StateMsg: (state) => state.Msg,
  StateIsLogIn: (state) => state.IsLogIn,
};

const actions = {
  async Register(context,form) {
    await axios.post('register', JSON.parse(JSON.stringify(form)))
    .then(function (response) {
      context.commit("setMsg",response.data.msg)
    })
    .catch(() => {
      context.commit("setMsg","Connection Error")
    });
  },

  async LogIn(context, form) {
    await axios.post("login", JSON.parse(JSON.stringify(form)))
    .then((response)=>
    {
      if (response.data.msg == "Logged in successfully!"){
        context.commit("setIsLogIn",true)
      }
      else{
        context.commit("setMsg",response.data.msg)
      }
    })
  },

  LogOut(context){
    context.commit("setIsLogIn",false)
  }
/*
  async CreatePost({ dispatch }, post) {
    await axios.post("post", post);
    return await dispatch("GetPosts");
  },

  async GetPosts({ commit }) {
    let response = await axios.get("posts");
    commit("setPosts", response.data);
  },

  async LogOut({ commit }) {
    let user = null;
    commit("logout", user);
  },*/
};

const mutations = {
  setIsLogIn(state, islogin) {
    state.IsLogIn = islogin;
  },
  setUsername(state, username) {
    state.Username = username;
  },
  setFirstName(state,firstname){
    state.FirstName = firstname
  },
  setLastName(state,lastname){
    state.LastName = lastname
  },
  setNickname(state,nickname){
    state.Nickname = nickname
  },
  setEmail(state,email){
    state.Email = email
  },
  setTel(state,tel){
    state.Tel = tel
  },
  setTag(state,tag){
    state.Tag = tag
  },
  setRating(state,rating){
    state.Rating = rating
  },
  setCheckin(state,checkin){
    state.Checkin = checkin
  },
  setFavorite(state,favorite){
    state.Favorite = favorite
  },
  setRole(state,role){
    state.Role = role
  },
  setMsg(state, msg){
    state.Msg = msg
  }
};

export default {
  state,
  getters,
  actions,
  mutations,
};