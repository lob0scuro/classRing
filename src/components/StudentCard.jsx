import React from "react";
import PointsButtonBlock from "./Buttons/PointsButtonBlock";

const StudentCard = ({ name }) => {
  const colors = {
    blue: ["#c5eaf7", "#1d4250"],
    pink: ["#fcd8fc", "#c957bd"],
    orange: ["#f06d22", "#8a3c0e"],
    green: ["#d4df90", "#87933c"],
  };

  const svgStyles = {
    width: "100%",
    height: "100%",
    fill: "none",
    stroke: colors.pink[1],
    strokeWidth: "25",
    strokeLinecap: "round",
    strokeLinejoin: "round",
    strokeMiterlimit: "10",
    strokeDasharray: "0",
    strokeDashoffset: "0",
    opacity: "1",
  };

  const cardStyles = {
    backgroundColor: "var(--saturatedPink)",
    width: "21rem",
    height: "25rem",
    margin: "10% auto",
    display: "flex",
    flexDirection: "column",
    border: "2px solid var(--saturatedPink)",
  };

  const circleStyles = {
    width: "100%",
    height: "75%",
    backgroundColor: "var(--pastelPink)",
  };

  const infoBlockStyles = {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    gap: "10px",
    padding: "10px",
  };

  return (
    <div style={cardStyles}>
      <div style={circleStyles}>
        <svg style={svgStyles} width="100%" height="100%">
          <circle r="35%" cx="50%" cy="50%" />
        </svg>
      </div>
      <div style={infoBlockStyles}>
        <h5 style={{ textAlign: "center", fontSize: "2rem" }}>{name}</h5>
        <PointsButtonBlock />
      </div>
    </div>
  );
};

export default StudentCard;
