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
  getQuizInfo() {
    return instance.get("/quiz-info");
  },
  getQuestion(position) {
    return instance.get("questions?position=" + position);
  },
  getQuestionById(id) {
    return instance.get("questions/" + id);
  },
  postParticipation(playerName, answers) {
    let answer = {
      playerName: playerName,
      answers: answers,
    };
    return instance.post("participations", answer);
  },
  login(username, password) {
    return instance.post("/login", { username, password });
  },
  getAllQuestion() {
    return instance.get("/questions/all", { withCredentials: true });
  },
  deleteQuestion(id) {
    return instance.delete("/questions/" + id, { withCredentials: true });
  },
  deleteAllQuestions() {
    return instance.delete("/questions/all", { withCredentials: true });
  },
  async editQuestion(question) {
    const vQuestion = JSON.parse(question);
    const response = await instance.put(
      "/questions/" + vQuestion.id,
      question,
      {
        withCredentials: true,
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    return response;
  },
};
