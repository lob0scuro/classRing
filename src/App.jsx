import { useState } from "react";
import Header from "./components/Header.jsx";
import LoginForm from "./components/LoginForm.jsx";
import StudentCard from "./components/StudentCard.jsx";
import Dashboard from "./components/Dashboard/Dashboard.jsx";

//color themes for student cards
const colors = {
  blue: ["#c5eaf7", "#1d4250"],
  pink: ["#fcd8fc", "#c957bd"],
  orange: ["#f06d22", "#8a3c0e"],
  green: ["#d4df90", "#87933c"],
};

//temp list of students for development
const students = [
  { name: "Claire", color: colors.pink, isActive: true },
  { name: "Max", color: colors.blue, isActive: true },
  { name: "Ezra", color: colors.pink, isActive: true },
  { name: "Evan", color: colors.green, isActive: true },
  { name: "Maddie", color: colors.orange, isActive: true },
  { name: "Lainey", color: colors.pink, isActive: true },
  { name: "Claire", color: colors.pink, isActive: true },
  { name: "Max", color: colors.blue, isActive: true },
  { name: "Ezra", color: colors.pink, isActive: true },
  { name: "Evan", color: colors.green, isActive: true },
  { name: "Maddie", color: colors.orange, isActive: true },
  { name: "Lainey", color: colors.pink, isActive: true },
];

function App() {
  //call backend api
  const [firstName, setFirstName] = useState("bill");
  const [lastName, setLastName] = useState("green");
  const getStudentInfo = async (e) => {
    e.preventDefault();

    data = { sid };

    url = "http://127.0.0.1:5000/api/get_student/6";

    body = JSON.stringify(data);

    const callAPI = await fetch(url);
    if (callAPI.status !== 201 && callAPI.status !== 200) {
      const data = await callAPI.json();
      alert(data.message);
    } else {
      // do something else (CURRENT TAKS)
    }
  };

  //map through the students and create student card compnents
  const cards = students.map((student) => {
    return <StudentCard name={student.name} color={student.color} />;
  });

  return (
    <>
      <Header />
      <form onSubmit={getStudentInfo}>
        <input
          type="number"
          onChange={(e) => {
            e.target.value;
          }}
        />
        <button type="submit">get </button>
      </form>
      <ul style={{ textAlign: "center" }}>
        <li>{firstName}</li>
        <li>{lastName}</li>
      </ul>
      {/*
      <LoginForm />
      <Dashboard students={students} colors={colors} />
      {cards}
      */}
    </>
  );
}

export default App;
