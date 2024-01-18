-- File: Task 100
-- Creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Create Stored Procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN in_user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    DECLARE average_weighted_score FLOAT;

    -- Calculate total weighted score and total weight
    SELECT 
        SUM(c.score * p.weight),
        SUM(p.weight)
    INTO 
        total_weighted_score,
        total_weight
    FROM 
        corrections c
    JOIN 
        projects p ON c.project_id = p.id
    WHERE 
        c.user_id = in_user_id;

    -- Avoid division by zero
    IF total_weight > 0 THEN
        -- Calculate average weighted score
        SET average_weighted_score = total_weighted_score / total_weight;

        -- Update the average_score for the user
        UPDATE users
        SET average_score = average_weighted_score
        WHERE id = in_user_id;
    END IF;
END;
//
DELIMITER ;
