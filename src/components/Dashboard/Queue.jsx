import React from "react";

const Queue = ({ name, color }) => {
  const container = {
    padding: "5%",
    margin: "5%",
    display: "flex",
    alignItems: "flex-end",
  };

  const circleStyles = {
    width: "5rem",
    height: "5rem",
    backgroundColor: color[1],
    borderRadius: "50%",
  };

  const nameBlock = {
    display: "flex",
    gap: "5px",
  };

  const buttonStyles = {
    borderRadius: "50%",
    border: "none",
    fontWeight: "700",
    fontSize: "1rem",
    color: "red",
    backgroundColor: "transparent",
  };
  return (
    <div style={container}>
      <div style={circleStyles}></div>
      <div style={nameBlock}>
        <p>
          <strong>{name}</strong>
        </p>
        <button style={buttonStyles}>x</button>
      </div>
    </div>
  );
};

export default Queue;
