const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

const API = {
  CHATBOT: `${BACKEND_URL}/api/chatbot`,
  QGEN: `${BACKEND_URL}/api/qgen`,
  SCORING: `${BACKEND_URL}/api/scoring`,
  WRITE_PROFREADING: `${BACKEND_URL}/api/write_profreading`,
};

export default API;
