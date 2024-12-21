import React from "react";

const Equity = ({ equity }) => {
    return (
        <div className="section equity">
            <h3>Equity</h3>
            <ul>
                <li>Retained Earnings: ${equity.retained}</li>
                <li>Capital: ${equity.capital}</li>
            </ul>
        </div>
    );
};

export default Equity;
