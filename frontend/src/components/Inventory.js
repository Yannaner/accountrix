import React from "react";

const Inventory = ({ inventory }) => {
    return (
        <div className="section inventory">
            <h3>Inventory</h3>
            <ul>
                <li>Finished Goods: {inventory.fg}</li>
                <li>WIP: {inventory.wip}</li>
                <li>Raw Material: {inventory.rawMaterial}</li>
            </ul>
        </div>
    );
};

export default Inventory;
