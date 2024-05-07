import React from "react";
import styles from "./student-card.module.css";
import PointsButtonBlock from "./Buttons/PointsButtonBlock";

const StudentCard = () => {
  const svgStyles = {
    width: "100%",
    height: "100%",
    fill: "none",
    stroke: "var(--saturatedPink)",
    strokeWidth: "25",
    strokeLinecap: "round",
    strokeLinejoin: "round",
    strokeMiterlimit: "10",
    strokeDasharray: "0",
    strokeDashoffset: "0",
    opacity: "1",
  };

  return (
    <div className={styles.studentCard}>
      <div className={styles.circle}>
        <svg style={svgStyles} width="100%" height="100%">
          <circle r="35%" cx="50%" cy="50%" />
        </svg>
      </div>
      <div className={styles.infoBlock}>
        <h5>Claire</h5>
        <PointsButtonBlock />
      </div>
    </div>
  );
};

export default StudentCard;
