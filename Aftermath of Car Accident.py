def calculate_speed(t, d, v_limit):
    # Convert speed limit from mph to feet per second
    v_limit_fps = v_limit * 5280 / 3600
    
    # Calculate the speed of the car in feet per second
    speed_fps = d / t
    
    # Convert the speed of the car from feet per second to mph
    speed_mph = speed_fps * 3600 / 5280
    
    return speed_mph

def main():
    print("Please enter the following information:")
    t = float(input("Time taken to come to a halt (seconds): "))
    d = float(input("Distance traveled during the skid (feet): "))
    v_limit = float(input("Speed limit (miles per hour): "))

    speed_mph = calculate_speed(t, d, v_limit)

    print(f"The speed of the car at the time of the accident was approximately {speed_mph:.10f} mph.")

    if speed_mph > v_limit:
        print("The driver was speeding.")
    else:
        print("The driver was not speeding.")

if __name__ == "__main__":
    main()
