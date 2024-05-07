import React from "react";

const Header = () => {
  const styles = {
    color: "var(--lightAqua)",
    backgroundColor: "var(--darkAqua)",
    fontSize: "3rem",
    textAlign: "center",
    padding: "5% 10%",
    boxShadow: "0 8px 12px -2px rgba(0, 0, 0, 0.8)",
  };
  return (
    <header>
      <h1 style={styles}>classRing</h1>
    </header>
  );
};

export default Header;
