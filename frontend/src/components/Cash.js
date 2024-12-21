import React from "react";

const Cash = ({ cash }) => {
    return (
        <div className="section center cash">
            <h3>Cash</h3>
            <h1>${cash}</h1>
        </div>
    );
};

export default Cash;
