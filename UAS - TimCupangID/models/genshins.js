const {sequelize, DataTypes} = require("./model.js");

const Genshin = sequelize.define('genshins', {
    icon : DataTypes.STRING,
    name : DataTypes.STRING,
    weapontype : DataTypes.STRING,
    base : DataTypes.STRING,
    substat : DataTypes.STRING
})

module.exports = Genshin;
// export default Genshin;