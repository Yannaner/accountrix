import React from "react";

const Liabilities = ({ liabilities }) => {
    return (
        <div className="section liabilities">
            <h3>Liabilities</h3>
            <ul>
                <li>Loan: ${liabilities.loan}</li>
                <li>Interest: ${liabilities.interest}</li>
                <li>Other Liability: ${liabilities.other}</li>
            </ul>
        </div>
    );
};

export default Liabilities;
