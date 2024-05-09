import React from "react";
import styles from "./button-bar.module.css";

const PointsButtonBlock = ({ clr }) => {
  const buttonStyles = {
    backgroundColor: clr[0],
    fontSize: "1.2rem",
    fontWeight: "600",
    padding: "8px",
    color: clr[1],
    border: "2px solid " + clr[1],
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
