import React from "react";
import styles from "./button-bar.module.css";

const PointsButtonBlock = () => {
  const buttonStyles = {
    backgroundColor: "var(--pastelPink)",
    fontSize: "1.2rem",
    fontWeight: "600",
    padding: "8px",
    color: "var(--saturatedPink)",
    border: "2px solid var(--saturatedPink)",
  };
  return (
    <div className={styles.btnBlock}>
      <button className={styles.btn} style={buttonStyles}>
        -10
      </button>
      <button className={styles.btn} style={buttonStyles}>
        -5
      </button>
      <button className={styles.btn} style={buttonStyles}>
        +5
      </button>
      <button className={styles.btn} style={buttonStyles}>
        +10
      </button>
    </div>
  );
};

export default PointsButtonBlock;
