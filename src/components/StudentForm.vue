<template>
  <h2 class="text-centered">Student<br />Registration</h2>
  <form action="#">
    <label for="username"
      >Username

      <input type="text" name="username" id="username" />
    </label>
    <label for="color"> Color <input type="color" /> </label>
    <label for="class">
      Class:
      <select name="class" id="class">
        <option value="null"></option>
        <option value="teacher1">teacher1</option>
        <option value="teacher2">teacher2</option>
        <option value="teacher3">teacher3</option>
        <option value="teacher4">teacher4</option>
        <option value="teacher5">teacher5</option>
        <option value="teacher6">teacher6</option>
        <option value="teacher7">teacher7</option>
        <option value="teacher8">teacher8</option>
      </select>
    </label>
    <label for="student">
      Name:
      <select name="class" id="class">
        <option value="null"></option>
        <option value="student1">student1</option>
        <option value="student2">student2</option>
        <option value="student3">student3</option>
        <option value="student4">student4</option>
        <option value="student5">student5</option>
        <option value="student6">student6</option>
        <option value="student7">student7</option>
        <option value="student8">student8</option>
        <option value="student9">student9</option>
        <option value="student10">student10</option>
      </select>
    </label>
    <label for="image"> Upload Image </label>
    <input type="file" />
    <input type="submit" value="Queue Up" />
  </form>
</template>

<style scoped>
h2 {
  text-decoration: underline;
  font-size: 1.8rem;
  margin: 0 auto 15px auto;
}

form {
  display: grid;
  grid-template-columns: 1fr;

  gap: 10px;
  text-align: center;

  background-color: var(--primary1);
  color: var(--secondary1);
  font-size: 1.5rem;

  width: min-content;
  margin: 0 auto;
  padding: 1rem 1.2rem;

  border: 2px solid var(--secondary1);
  border-radius: 10px;
  box-shadow: -9px 10px 2.5px var(--primary2);
}

input#username {
  width: 45%;
}

label[for="image"] {
  margin-top: 25px;
  padding-top: 3px;
  border-top: 2px solid var(--primary2);
}
input::file-selector-button {
  color: var(--primary1);
  width: fit-content;
}

input[type="submit"] {
  width: 50%;
  margin: 20px auto 0 auto;
  text-align: center;
  border: none;
  border-radius: 25px;
  padding: 10px;
  box-shadow: -4px 4px 8px -1px rgba(0, 0, 0, 0.5);

  background-color: var(--primary2);
}
input[type="submit"]:active {
  box-shadow: -1px 1px 4px 0 rgba(0, 0, 0, 0.8);
  background-color: var(--secondary1);
  color: var(--primary2);
}
</style>
