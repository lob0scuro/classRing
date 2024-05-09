import React from "react";
import Queue from "./Queue";

const Dashboard = ({ students, colors }) => {
  const mainContainer = {
    display: "flex",
    flexWrap: "wrap",
  };

  const adminStyles = {
    width: "fit-content",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    borderBottom: "1px solid",
    borderRight: "1px solid",
    margin: "5%",
    padding: "3%",
  };

  const svgStyles = {
    width: "20rem",
    height: "20rem",
    fill: "none",
    stroke: colors.blue[1],
    strokeWidth: "25",
    strokeLinecap: "round",
    strokeLinejoin: "round",
    strokeMiterlimit: "10",
    strokeDasharray: "0",
    strokeDashoffset: "0",
    opacity: "1",
  };

  const circleStyles = {
    width: "20rem",
    height: "20rem",
    borderRadius: "50%",
  };

  const formStyles = {
    display: "flex",
    flexDirection: "column",
  };

  const renderStudents = students.map((student) => {
    if (student.isActive) {
      return <Queue name={student.name} color={student.color} />;
    }
  });

  const populateOptions = students.map((student) => {
    return <option value={student.name}>{student.name}</option>;
  });

  return (
    <>
      <div style={mainContainer}>
        <div className="adminBlock" style={adminStyles}>
          <div style={circleStyles}>
            <svg style={svgStyles} width="25rem" height="25rem">
              <circle r="35%" cx="50%" cy="50%" />
            </svg>
          </div>
          <p id="greeting">Hello, Teacher</p>
          <form action="#" style={formStyles}>
            <select
              name="active-students"
              id="active-students"
              size="4"
              multiple
            >
              {populateOptions}
            </select>

            <input type="submit" value="Activate" />
            <p>
              <small>hold ctl to select multiple students</small>
            </p>
          </form>
        </div>
        {renderStudents}
      </div>
    </>
  );
};

export default Dashboard;
