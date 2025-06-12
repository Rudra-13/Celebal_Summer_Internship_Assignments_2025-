SELECT hackers.hacker_id, hackers.name
FROM hackers
JOIN (
  SELECT submissions.hacker_id, COUNT(DISTINCT submissions.challenge_id) AS full_score_count
  FROM submissions
  JOIN challenges ON submissions.challenge_id = challenges.challenge_id
  JOIN difficulty ON challenges.difficulty_level = difficulty.difficulty_level
  WHERE submissions.score = difficulty.score
  GROUP BY submissions.hacker_id
  HAVING COUNT(DISTINCT submissions.challenge_id) > 1
) AS full_scores
ON hackers.hacker_id = full_scores.hacker_id
ORDER BY full_scores.full_score_count DESC, hackers.hacker_id ASC;