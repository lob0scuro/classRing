import React from "react";

const LoginForm = () => {
  const formStyles = {
    display: "flex",
    flexDirection: "column",
    gap: "25px",
    width: "fit-content",
    margin: "20% auto 0 auto",
    backgroundColor: "var(--darkAqua)",
    color: "var(--lightAqua)",
    padding: "5%",
    boxShadow: "-8px 8px rgba(0, 0, 0, 0.5)",
    borderRadius: ".5rem",
  };

  const legendStyles = {
    textAlign: "center",
    fontSize: "2.5rem",
    color: "var(--lightAqua)",
  };

  const labelStyles = {
    fontSize: "1.2rem",
    fontWeight: "700",
  };

  const inputStyles = {
    fontSize: "1.4rem",
    padding: "8px",
    borderRadius: ".5rem",
    backgroundColor: "var(--pastelMoss)",
    color: "var(--saturatedMoss)",
  };

  const buttonStyles = {
    backgroundColor: "var(--saturatedMoss)",
    color: "inherit",
    fontSize: "1.5rem",
    fontWeight: "900",
    width: "fit-content",
    margin: "0 auto",
    fontFamily: "inherit",
    padding: "10px",
    borderRadius: ".5rem",
  };

  return (
    <form style={formStyles} action="#">
      <legend style={legendStyles}>Login</legend>
      <label style={labelStyles} htmlFor="username">
        Username
      </label>
      <input style={inputStyles} type="number" placeholder="username" />
      <label style={labelStyles} htmlFor="password">
        Password
      </label>
      <input style={inputStyles} type="password" placeholder="password" />
      <input type="submit" value="Login" style={buttonStyles} />
    </form>
  );
};

export default LoginForm;
