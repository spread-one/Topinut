import React from "react";
import { Link } from "react-router-dom";

function Header() {
  return (
    <header style={styles.header}>
      <div style={styles.logo}>
        <h1>TOPINUT</h1>
      </div>
      <nav>
        <ul style={styles.navList}>
          <li style={styles.navItem}><Link to="/correct" style={styles.link}>문제 첨삭</Link></li>
          <li style={styles.navItem}><Link to="/generate" style={styles.link}>문제 받기</Link></li>
          <li style={styles.navItem}><Link to="/weakness" style={styles.link}>내 약점 파악하기</Link></li>
          <li style={styles.navItem}><Link to="/chatbot" style={styles.link}>토픽 챗봇</Link></li>
        </ul>
      </nav>
    </header>
  );
}

const styles = {
  header: { display: "flex", justifyContent: "space-between", padding: "10px 20px", backgroundColor: "#F85D3A", color: "#fff" },
  logo: { fontSize: "1.5em", fontWeight: "bold" },
  navList: { listStyle: "none", display: "flex", margin: 0, padding: 0 },
  navItem: { marginLeft: "20px" },
  link: { textDecoration: "none", color: "#fff", fontWeight: "bold" },
};

export default Header;
