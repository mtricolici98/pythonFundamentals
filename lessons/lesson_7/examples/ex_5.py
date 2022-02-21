def custom_multiple_input(prompts: list, times=1):
    # Storing our results
    results = []
    for a in range(times):
        # Storing input data for this time
        user_input_data = dict()
        for prompt in prompts:
            # Adding input value from user to prompt key
            user_input_data[prompt] = input(f'Input {prompt}: ')
        # Adding the dict with our input values to results
        results.append(user_input_data)
        # Returning results
    return results


custom_multiple_input(['first name', 'last name'], 2) 
