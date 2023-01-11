import User from "../models/user.js";
const login = (req, res, next) => {
  let msg = req.session.err || "";
  req.session.err = "";
  res.render("login", { user: req.session.user || "", message: msg });
};
const logout = (req, res, next) => {
  req.session.destroy();
  res.redirect("/");
};
const auth = (req, res, next) => {
  const data = {
    email: req.body.email,
    password: req.body.password,
  };
  req.session.err = "";
  User.findOne({ where: { email: data.email } })
    .then((results) => {
      if (!results) {
        req.session.err = "Incorrect email or password.";
        res.redirect("/login");
      } else if (data.password != results.password) {
        req.session.err = "Incorrect password.";
        res.redirect("/login");
      } else {
        req.session.user = results;
        res.redirect("/");
      }
    })
    .catch((err) => {
      req.session.err = err;
      res.redirect("/login");
    });
};
export default { login, logout, auth };
