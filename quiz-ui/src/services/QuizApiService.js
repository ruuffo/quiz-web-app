import axios from "axios";
import ServiceAdminController from "./ServiceAdminController";
const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true,
});
instance.interceptors.request.use((config) => {
  const token = ServiceAdminController.getToken();
  if (token) {
    config.headers.Authorization = "Bearer " + token;
  }
  return config;
});
export default {
  // async call(method, resource, data = null) {
  //   var headers = {
  //     "Content-Type": "application/json",
  //   };

  //   if (token != null) {
  //     headers.authorization = "Bearer " + token;
  //   }

  //   return instance({
  //     method,
  //     headers: headers,
  //     url: resource,
  //     data,
  //   })
  //     .then((response) => {
  //       return { status: response.status, data: response.data };
  //     })
  //     .catch((error) => {
  //       console.error(error);
  //     });
  // },
  getQuizInfo() {
    return instance.get("/quiz-info");
    // return this.call("get", "quiz-info");
    //récupérer le tableau des scores et le nombre total de questions du quiz.
  },
  getQuestion(position) {
    return instance.get("questions?position=" + position);
    // return this.call("get", "questions?position=" + position);
    // not implemented
  },
  postParticipation(playerName, answers) {
    let answer = {
      playerName: playerName,
      answers: answers,
    };
    return instance.post("participations", answer);
    // return this.call("post", "participations", answer);
  },
  login(username, password) {
    return instance.post("/login", { username, password });
  },
  getAllQuestion() {
    return instance.get("/questions/all", { withCredentials: true });
  },
};
