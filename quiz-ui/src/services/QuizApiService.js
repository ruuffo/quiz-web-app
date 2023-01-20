import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
    //récupérer le tableau des scores et le nombre total de questions du quiz.
  },
  getQuestion(position) {
    return this.call("get", "questions?position=" + position);
    // not implemented
  },
  postParticipation(playerName, answers) {
    let answer = {
      "playerName": playerName,
      "answers": answers
    }
    return this.call("post", "participations", answer);
  }
};