import React from "react";

const OperationCosts = ({ costs }) => {
    return (
        <div className="section operation-costs">
            <h3>Operation Costs</h3>
            <ul>
                <li>R&D: ${costs.rnd}</li>
                <li>Selling: ${costs.selling}</li>
                <li>Marketing: ${costs.marketing}</li>
                <li>Admin: ${costs.admin}</li>
            </ul>
        </div>
    );
};

export default OperationCosts;
