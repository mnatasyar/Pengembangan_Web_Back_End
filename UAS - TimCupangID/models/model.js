// import { Sequelize, DataTypes } from "sequelize";

const { Sequelize, DataTypes } = require('sequelize');

const sequelize = new Sequelize("db_genshin", "root", "", {
    host : 'localhost',
    dialect : 'mysql',
    port : '3307'
});

const authenticate = () => {
    sequelize
      .authenticate()
      .then(() => {
        console.log('Connection has been established successfully.');
      })
      .catch((err) => {
        console.error('Unable to connect to the database:', err);
      });
};

module.exports = {sequelize, DataTypes, authenticate};

// export {sequelize, DataTypes};