import React from "react";
import PointsButtonBlock from "./Buttons/PointsButtonBlock";

const StudentCard = ({ name, color }) => {
  const svgStyles = {
    width: "100%",
    height: "100%",
    fill: "none",
    stroke: color[1],
    strokeWidth: "25",
    strokeLinecap: "round",
    strokeLinejoin: "round",
    strokeMiterlimit: "10",
    strokeDasharray: "0",
    strokeDashoffset: "0",
    opacity: "1",
  };

  const cardStyles = {
    backgroundColor: color[1],
    width: "21rem",
    height: "25rem",
    margin: "10% auto",
    display: "flex",
    flexDirection: "column",
    border: `2px solid` + color[1],
  };

  const circleStyles = {
    width: "100%",
    height: "75%",
    backgroundColor: color[0],
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
        <h5
          style={{
            textAlign: "center",
            fontSize: "2rem",
            color: "#fefefe",
            textShadow: "-2px 2px 3px rgba(0,0,0,0.8)",
          }}
        >
          {name}
        </h5>
        <PointsButtonBlock clr={color} />
      </div>
    </div>
  );
};

export default StudentCard;
