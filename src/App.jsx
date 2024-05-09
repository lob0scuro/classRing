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
  //map through the students and create student card compnents
  const cards = students.map((student) => {
    return <StudentCard name={student.name} color={student.color} />;
  });

  return (
    <>
      <Header />
      <LoginForm />
      {/*
      <Dashboard students={students} colors={colors} />
      {cards}
      */}
    </>
  );
}

export default App;
