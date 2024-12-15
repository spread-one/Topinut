import React from "react";
import Header from "../components/Header";

function Home() {
  return (
    <div>
      {/* 헤더 컴포넌트 */}
      <Header />

      {/* 헤더 아래 공백 */}
      <div style={styles.blankSpace}></div>
    </div>
  );
}

const styles = {
  blankSpace: {
    height: "500px", // 공백의 높이를 설정
    backgroundColor: "#f9f9f9", // 공백 영역의 배경색
  },
};

export default Home;
