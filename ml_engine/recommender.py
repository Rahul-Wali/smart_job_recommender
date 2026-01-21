"""
Machine Learning Job Recommendation Engine

This module implements a content-based recommendation system using:
- TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization
- Cosine Similarity for measuring text similarity

The algorithm compares user skills with job requirements to recommend relevant positions.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class JobRecommender:
    """
    A content-based job recommendation system using TF-IDF and Cosine Similarity.
    
    How it works:
    1. Converts user skills and job requirements into TF-IDF vectors
    2. Calculates cosine similarity between user vector and all job vectors
    3. Ranks jobs by similarity score (0 to 1, where 1 is perfect match)
    """
    
    def __init__(self):
        """
        Initialize the recommender with a TF-IDF vectorizer.
        """
        # TfidfVectorizer converts text into numerical feature vectors
        # - lowercase=True: converts all text to lowercase for consistency
        # - stop_words='english': removes common words like 'the', 'is', etc.
        # - ngram_range=(1,2): considers both single words and word pairs
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words='english',
            ngram_range=(1, 2),
            max_features=1000
        )
    
    def preprocess_skills(self, skills_text):
        """
        Clean and normalize skills text for better matching.
        
        Args:
            skills_text (str): Raw skills text (comma-separated)
        
        Returns:
            str: Cleaned and normalized skills text
        """
        if not skills_text:
            return ""
        
        # Convert to lowercase and remove extra spaces
        skills_text = skills_text.lower().strip()
        
        # Replace commas with spaces for better tokenization
        skills_text = skills_text.replace(',', ' ')
        
        return skills_text
    
    def calculate_match_percentage(self, similarity_score):
        """
        Convert similarity score to percentage.
        
        Args:
            similarity_score (float): Cosine similarity score (0 to 1)
        
        Returns:
            int: Match percentage (0 to 100)
        """
        return int(similarity_score * 100)
    
    def get_recommendations(self, user_skills, jobs_queryset, top_n=20):
        """
        Generate job recommendations based on user skills.
        
        Args:
            user_skills (str): User's skills as comma-separated text
            jobs_queryset (QuerySet): Django QuerySet of Job objects
            top_n (int): Number of top recommendations to return
        
        Returns:
            list: List of dictionaries containing job objects and similarity scores
        """
        # Handle edge cases
        if not user_skills or not user_skills.strip():
            return []
        
        if not jobs_queryset or jobs_queryset.count() == 0:
            return []
        
        # Preprocess user skills
        user_skills_clean = self.preprocess_skills(user_skills)
        
        # Prepare job skills corpus
        job_skills_list = []
        jobs_list = list(jobs_queryset)
        
        for job in jobs_list:
            job_skills = self.preprocess_skills(job.required_skills)
            job_skills_list.append(job_skills)
        
        # Create corpus: user skills + all job skills
        corpus = [user_skills_clean] + job_skills_list
        
        try:
            # Step 1: Convert text to TF-IDF vectors
            tfidf_matrix = self.vectorizer.fit_transform(corpus)
            
            # Step 2: Calculate cosine similarity
            # User vector is the first row (index 0)
            user_vector = tfidf_matrix[0:1]
            
            # Job vectors start from index 1
            job_vectors = tfidf_matrix[1:]
            
            # Calculate similarity between user and all jobs
            similarity_scores = cosine_similarity(user_vector, job_vectors)[0]
            
            # Step 3: Create recommendation list with jobs and scores
            recommendations = []
            for idx, job in enumerate(jobs_list):
                similarity_score = similarity_scores[idx]
                match_percentage = self.calculate_match_percentage(similarity_score)
                
                recommendations.append({
                    'job': job,
                    'similarity_score': float(similarity_score),
                    'match_percentage': match_percentage,
                    'confidence': self._get_confidence_level(similarity_score)
                })
            
            # Step 4: Sort by similarity score (descending) and return top N
            recommendations.sort(key=lambda x: x['similarity_score'], reverse=True)
            
            return recommendations[:top_n]
        
        except Exception as e:
            # Handle any errors gracefully
            print(f"Error in recommendation engine: {str(e)}")
            return []
    
    def _get_confidence_level(self, similarity_score):
        """
        Categorize the match quality based on similarity score.
        
        Args:
            similarity_score (float): Cosine similarity score
        
        Returns:
            str: Confidence level description
        """
        if similarity_score >= 0.7:
            return "Excellent Match"
        elif similarity_score >= 0.5:
            return "Good Match"
        elif similarity_score >= 0.3:
            return "Fair Match"
        else:
            return "Low Match"
    
    def explain_recommendation(self, user_skills, job_skills):
        """
        Provide explanation for why a job was recommended.
        
        Args:
            user_skills (str): User's skills
            job_skills (str): Job's required skills
        
        Returns:
            dict: Explanation details including matching skills
        """
        user_skills_set = set(skill.strip().lower() for skill in user_skills.split(',') if skill.strip())
        job_skills_set = set(skill.strip().lower() for skill in job_skills.split(',') if skill.strip())
        
        # Find matching skills
        matching_skills = user_skills_set.intersection(job_skills_set)
        missing_skills = job_skills_set.difference(user_skills_set)
        
        return {
            'matching_skills': list(matching_skills),
            'missing_skills': list(missing_skills),
            'match_count': len(matching_skills),
            'total_required': len(job_skills_set)
        }
