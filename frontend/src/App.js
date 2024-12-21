import React, { useState, useEffect } from "react";
import axios from "axios";
import Cash from "./components/Cash";
import Inventory from "./components/Inventory";
import OperationCosts from "./components/OperationCosts";
import Assets from "./components/Assets";
import Liabilities from "./components/Liabilities";
import Equity from "./components/Equity";

const App = () => {
   const [data, setData] = useState(null);

   useEffect(() => {
       axios.get("/api/dashboard")
           .then((response) => setData(response.data))
           .catch((error) => console.error(error));
   }, []);

   if (!data) return <div>Loading...</div>;

   return (
       <div className="board">
           <Inventory inventory={data.inventory} />
           <OperationCosts costs={data.costs} />
           <Cash cash={data.cash} />
           <Assets assets={data.assets} />
           <Liabilities liabilities={data.liabilities} />
           <Equity equity={data.equity} />
       </div>
   );
};

export default App;
