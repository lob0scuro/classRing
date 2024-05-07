import React from "react";
import styles from "./student-card.module.css";

const StudentCard = () => {
  return (
    <div className={styles.studentCard}>
      <div className={styles.circle}></div>
      <div className={styles.infoBlock}>
        <h5>Claire</h5>
        <div className={styles.controllerBlock}>
          <button>-10</button>
          <button>-5</button>
          <button>+5</button>
          <button>+10</button>
        </div>
      </div>
    </div>
  );
};

export default StudentCard;
