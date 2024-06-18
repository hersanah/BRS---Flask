document.addEventListener('DOMContentLoaded', function() {
    const welcomeButton = document.getElementById('welcome-button');
    const googleSignupButton = document.getElementById('google-signup');
    const amazonSignupButton = document.getElementById('amazon-signup');
    const emailSignupButton = document.getElementById('email-signup');
    const signInButton = document.getElementById('signin-button'); // Added

    const welcomeScreen = document.getElementById('welcome-screen');
    const signupOptionsScreen = document.getElementById('signup-options-screen');
    const signinScreen = document.getElementById('signin-screen');
    const genderSelectionScreen = document.getElementById('gender-selection-screen');
    const genreSelectionScreen = document.getElementById('genre-selection-screen');
    const bookRecommendationsScreen = document.getElementById('book-recommendations-screen');
    const readingScreen = document.getElementById('reading-screen');

    welcomeButton.addEventListener('click', function() {
        welcomeScreen.classList.add('hidden');
        signupOptionsScreen.classList.remove('hidden');
    });

    googleSignupButton.addEventListener('click', function() {
        signupOptionsScreen.classList.add('hidden');
        genderSelectionScreen.classList.remove('hidden');
    });

    amazonSignupButton.addEventListener('click', function() {
        signupOptionsScreen.classList.add('hidden');
        genderSelectionScreen.classList.remove('hidden');
    });

    emailSignupButton.addEventListener('click', function() {
        signupOptionsScreen.classList.add('hidden');
        genderSelectionScreen.classList.remove('hidden');
    });

    // Event listener for sign-in button
    signInButton.addEventListener('click', function() {
        // Perform sign-in logic here
        console.log('Sign in button clicked');
       
    });

    // Add event listeners for other buttons as needed
});
