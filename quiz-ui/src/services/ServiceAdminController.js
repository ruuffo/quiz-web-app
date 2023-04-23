import router from "@/router";

export default {
  saveToken(token) {
    window.localStorage.setItem("token", token);
  },
  getToken() {
    return window.localStorage.getItem("token");
  },
  signOut() {
    window.localStorage.removeItem("token");
    router.push("/login");
  },
  setCurrentQuestionPosition(currentQuestion) {
    window.localStorage.setItem("currentQuestion", currentQuestion);
  },
  getCurrentQuestionPosition() {
    return window.localStorage.getItem("currentQuestion");
  },
  setCurrentQuestionId(currentQuestionId) {
    window.localStorage.setItem("currentQuestionId", currentQuestionId);
  },
  getCurrentQuestionId() {
    return window.localStorage.getItem("currentQuestionId");
  },
  saveNbQuestions(nbQuestions) {
    window.localStorage.setItem("nbQuestions", nbQuestions);
  },
  getNbQuestions() {
    return window.localStorage.getItem("nbQuestions");
  },
};
