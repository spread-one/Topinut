import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/correct" element={<h2>문제 첨삭 페이지</h2>} />
        <Route path="/generate" element={<h2>문제 받기 페이지</h2>} />
        <Route path="/weakness" element={<h2>내 약점 파악하기 페이지</h2>} />
        <Route path="/chatbot" element={<h2>토픽 챗봇 페이지</h2>} />
      </Routes>
    </Router>
  );
}

export default App;
